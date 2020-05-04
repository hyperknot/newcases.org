<script>
  import router from 'page'
  import ChartBoard from './ChartBoard.svelte'
  import Country from './Country.svelte'

  let page
  let params

  router('/', () => (page = ChartBoard))
  router(
    '/country/:id',
    (ctx, next) => {
      console.log(ctx, next)
      params = ctx.params
      next()
    },
    () => (page = Country)
  )

  router.start()
</script>

<svelte:component this={page} {params} />
