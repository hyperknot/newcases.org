export function createStore() {
  return {
    data: [],
    addData(item) {
      this.data.push(item)
    },
    removeData(item) {
      this.data.splice(this.data.indexOf(item), 1)
    },
  }
}
