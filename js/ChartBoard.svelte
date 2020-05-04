<script>
  import { onMount } from 'svelte'

  import Chart from './Chart.svelte'
  import data from '../data/country_data.json'

  let sortedDataEntries

  const dataEntries = Object.entries(data)

  sortedDataEntries = dataEntries.sort(([country1, country1Data], [country2, country2Data]) => {
    const country1Cases = Object.values(country1Data)
    const country1maxNumber = parseInt(country1Cases[country1Cases.length - 1])
    const country2Cases = Object.values(country2Data)
    const country2maxNumber = parseInt(country2Cases[country2Cases.length - 1])

    if (country1maxNumber > country2maxNumber) {
      return -1
    }

    if (country1maxNumber < country2maxNumber) {
      return 1
    }

    return 0
  })
</script>

<main>
  <div class="chart-container">
    {#if data}
      {#each sortedDataEntries as dataEntry}
        <a class="chart-wrapper" href="/country/{dataEntry[0]}">
          <h3>{dataEntry[0]}</h3>
          <Chart data={dataEntry[1]} period="14" />
        </a>
      {/each}
    {/if}
  </div>
</main>

<style>
  .chart-container {
    display: flex;
    flex-wrap: wrap;
  }

  .chart-wrapper {
    width: 50%;
    color: #000;
  }
</style>
