<script>
    import * as d3 from 'd3';
    import tip from 'd3-tip';
    import { onMount } from 'svelte';

    export let data;
    export let period;
    let chart;

    const countryEntries = Object.entries(data);
    const keep = period ? parseInt(period) * -1 : 0;
    const countryData = countryEntries.map(([date, cases], index) => {
      const newCases = index > 0 ? cases - countryEntries[index - 1][1] : parseInt(cases);
      return {
        date,
        cases,
        newCases
      }
    }).slice(keep);

    const margin = ({top: 20, right: 0, bottom: 50, left: 40});

    const width = 960;
    const height = 500;

    const y = d3.scaleLinear()
        .domain([0, d3.max(countryData, d => parseInt(d.newCases))])
        .range([height - margin.bottom, margin.top]);

    const x = d3.scaleBand()
        .domain(countryData.map(d => d.date))
        .rangeRound([margin.left, width - margin.right])
        .padding(0.1);


    const yAxis = g => g
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(y))
        .call(g => g.select(".domain").remove());

    const xAxis = g => g
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x).tickSize(0).tickValues([]));


    const tooltip = tip().attr('class', 'd3-tip')
        .offset([-10, 0])
        .style('background', 'rgba(0, 0, 0, 0.8)')
        .style('color', '#fff')
        .style('padding', '8px')
        .style('font-size', '14px')
        .style('border-radius', '4px')
        .html(d => `date: <b>${d.date}</b><br>new cases: <b>${d.newCases}</b>`);

    onMount(() => {
      const chartSvg = d3.select(chart).attr("viewBox", [0, 0, width, height]);

      chartSvg.call(tooltip);

      chartSvg.append("g")
          .attr("fill", "#39f3bb")
        .selectAll("rect")
        .data(countryData)
        .join("rect")
          .attr("x", d => x(d.date))
          .attr("y", d => y(d.newCases))
          .attr("height", d => y(0) - y(d.newCases))
          .attr("width", x.bandwidth())
        .on('mouseover', tooltip.show)
        .on('mouseout', tooltip.hide);

      chartSvg.append("g").call(xAxis);

      chartSvg.append("g").call(yAxis);



    });
</script>

<main>
    <svg class="chart" bind:this={chart}></svg>
</main>


<style>

</style>
