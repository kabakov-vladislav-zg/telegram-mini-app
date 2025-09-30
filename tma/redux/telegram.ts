import { createSlice } from '@reduxjs/toolkit';
import { retrieveLaunchParams, retrieveRawInitData, retrieveRawLaunchParams } from '@telegram-apps/bridge';
import { init } from '@telegram-apps/sdk';

interface CounterState {
  user: object
  chat: object
}

let initialState: object = {}

try {
  init();
  const launchParams = retrieveLaunchParams(true);
  const ownerdata = JSON.parse(atob(launchParams?.ownerdata as string));
  initialState = { ...launchParams, ownerdata }
  console.log('LaunchParams:\n', launchParams)
  console.log('Data from bot:\n', initialState)
  console.log('RawLaunchParams:\n', retrieveRawLaunchParams())
  console.log('RawInitData:\n', retrieveRawInitData())
} catch(e) {
  console.log('Telegram errors:\n', e)
}

export const counterSlice = createSlice({
  name: 'telegram',
  // `createSlice` will infer the state type from the `initialState` argument
  initialState,
  reducers: {
    increment: (state) => {

    },
    decrement: (state) => {

    },
  },
})

export const { increment, decrement } = counterSlice.actions
export default counterSlice.reducer