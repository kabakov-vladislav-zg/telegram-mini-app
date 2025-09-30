import { configureStore } from '@reduxjs/toolkit';
import { retrieveLaunchParams, retrieveRawInitData } from '@telegram-apps/bridge';
import { init } from '@telegram-apps/sdk';

try {
  init();
  console.log('LaunchParams:\n', retrieveLaunchParams())
  console.log('retrieveRawInitData:\n', retrieveRawInitData())
} catch(e) {
  console.log('Telegram errors:\n', e)
}


const store = configureStore({
  reducer: {

  },
})

export default store;
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch