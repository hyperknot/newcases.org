import { observable, action, computed } from 'mobx'

export class AppStore {
  @observable chartsVisible = true
  @observable mapVisible = true

  @observable timeseriesData

  @action
  loadData() {
    const res = await fetch('/export/timeseries.json1')
    this.timeseriesData = await res.json()

    //
    // try {
    //   const res = await fetch('/export/timeseries.json1')
    //   this.timeseriesData = await res.json()
    // } catch (e) {
    //   console.error(`error loading timeseries.json: ${e}`)
    // }
  }
}

export default new AppStore()
