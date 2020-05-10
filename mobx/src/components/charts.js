import { observer } from 'mobx-react-lite'
import React from 'react'

import { useStores } from '../hooks/use-stores'

export const Charts = observer(() => {
  const { appStore } = useStores()

  return (
    <div id="charts">
      {/**/}
      {!appStore.timeseriesData ? <div>Loading</div> : <div>Charts</div>}
    </div>
  )
})
