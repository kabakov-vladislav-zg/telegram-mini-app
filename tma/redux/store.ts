import { configureStore } from '@reduxjs/toolkit';
import telegramReducer from './telegram';

const store = configureStore({
  reducer: {
    telegram: telegramReducer,
  },
})

export default store;
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch