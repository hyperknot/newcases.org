import { observer } from 'mobx-react-lite'
import React from 'react'
import { useStores } from '../hooks/use-stores'

export const Counter = observer(() => {
  const { appStore } = useStores()

  return (
    <>
      <div>{appStore.count}</div>
      <div>{appStore.doubleCount}</div>

      <button onClick={() => appStore.increment()}>++</button>
      <button onClick={() => appStore.decrement()}>--</button>
    </>
  )
})
