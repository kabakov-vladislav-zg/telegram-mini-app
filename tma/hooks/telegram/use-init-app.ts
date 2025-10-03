import { isTMA } from '@telegram-apps/bridge';
import { init } from '@telegram-apps/sdk';
import { useEffect, useState } from 'react';

export function useInitApp() {
  const [initialized, setInitialized] = useState(false);

  const checkIsTMA = async () => {
    if (!await isTMA('complete')) {
      const { appMockTelegramEnv } = await import(/* webpackChunkName: "mock" */ '@/mock/telegramEnv');
      appMockTelegramEnv();
    }
  }

  useEffect(() => {
    checkIsTMA().then(() => {
      init();
      setInitialized(true);
    });
  }, []);

  return initialized;
};