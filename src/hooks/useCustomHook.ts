import { useState, useEffect } from 'react'

export function useCustomHook() {
  const [value, setValue] = useState<string>('initial')

  useEffect(() => {
    // Any effect logic if needed
  }, [])

  function updateValue(newVal: string) {
    setValue(newVal)
  }

  return {
    value,
    updateValue
  }
}
