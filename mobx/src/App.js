import { observer } from 'mobx-react-lite'
import React, { useEffect } from 'react'

import './app.scss'
import { Charts } from './components/charts'
import { useStores } from './hooks/use-stores'

export const App = observer(() => {
  const { appStore } = useStores()

  useEffect(() => {
    try {
      appStore.loadData()
    } catch (e) {
      console.log('a')
    }
  }, [])

  return (
    <main>
      {appStore.chartsVisible && <Charts />}
      {appStore.mapVisible && <div id="map">map</div>}
    </main>
  )
})
