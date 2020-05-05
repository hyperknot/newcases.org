import { observer } from 'mobx-react-lite'
import React, { useState } from 'react'
import { useDataStore } from './context'

const MyComponent = observer(() => {
  const [query, setQuery] = useState('')
  const store = useDataStore()
  const { data, addData, removeData } = store
  const handleChange = (e) => {
    setQuery(e.target.value)
  }

  return (
    <div>
      <div>
        <input type="text" value={query} onChange={handleChange} />
        <button onClick={() => addData(query)}>Add data</button>
      </div>
      <ul>
        <button>Add data</button>

        {data.map((value) => (
          <li>
            <span>{value}</span>
            <button onClick={() => removeData(value)}>Remove data</button>
          </li>
        ))}
      </ul>
    </div>
  )
})

export default MyComponent
