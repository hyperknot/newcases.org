import React from 'react'
// import logo from './logo.svg'
import './App.css'
import { DataStoreProvider } from './context.js'
import MyComponent from './mycomponent.js'

function App() {
  return (
    <DataStoreProvider>
      <MyComponent />
    </DataStoreProvider>
  )
}

export default App
