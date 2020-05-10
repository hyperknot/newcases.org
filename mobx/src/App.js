import { observer } from 'mobx-react-lite'
import React from 'react'
import { Counter } from './components/counter.js'

import './app.scss'
import { useStores } from './hooks/use-stores'

export const App = observer(() => {
  const { appStore } = useStores()

  return (
    <main>
      {appStore.chartsVisible && <div id="charts">charts</div>}
      {appStore.mapVisible && <div id="map">map</div>}
    </main>
  )
})
