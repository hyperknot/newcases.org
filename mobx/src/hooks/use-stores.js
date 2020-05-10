import React from 'react'
import appStore from '../stores/app-store'

export const stores = {
  appStore,
}

window._debug = stores

console.log('use-stores.js')

const storesContext = React.createContext(stores)
export const useStores = () => React.useContext(storesContext)
