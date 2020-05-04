<script>
  import { onMount } from 'svelte'
  import router from 'page'
  import ChartBoard from './ChartBoard.svelte'
  import Country from './Country.svelte'

  let page
  let params
  let timeseries

  router('/', () => (page = ChartBoard))
  router(
    '/country/:id',
    (ctx, next) => {
      params = ctx.params
      next()
    },
    () => (page = Country)
  )
  router.start()

  onMount(async () => {
    try {
      const res = await fetch('/export/timeseries.json')
      timeseries = await res.json()
    } catch (e) {
      console.error(`error loading timeseries.json: ${e}`)
    }
  })
</script>

<svelte:component this={page} {params} />
