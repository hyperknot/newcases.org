<script>
  import Chart from './Chart.svelte'
  import data from '../data/country_data.json'

  export let params

  let country = params.id
</script>

<main>
  <h1>{country}</h1>
  <Chart data={data[country]} />
</main>

<style>
  main {
    width: 90%;
    margin: 0 auto;
  }
</style>
