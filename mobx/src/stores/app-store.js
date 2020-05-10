import { observable, action, computed } from 'mobx'

export class AppStore {
  @observable chartsVisible = true
  @observable mapVisible = true
}

export default new AppStore()
