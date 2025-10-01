import { useLaunchParams } from '@telegram-apps/sdk-react';

interface TgStartParam {
  id: number
  username: string
  first_name: string
  last_name: string
}

function decodeBase64Url<T extends object>(encodedStr: string): T {
  let padding = encodedStr.length % 4;
  if (padding !== 0) {
      encodedStr += '='.repeat(4 - padding);
  }
  const base64 = encodedStr.replace(/-/g, '+').replace(/_/g, '/');
  const jsonStr = atob(base64);
  return JSON.parse(jsonStr);
}

export function useTgStartParam() {
  console.log('useLaunchParams\n', useLaunchParams())
  const { tgWebAppStartParam } = useLaunchParams();

  return decodeBase64Url<TgStartParam>(tgWebAppStartParam!)
}