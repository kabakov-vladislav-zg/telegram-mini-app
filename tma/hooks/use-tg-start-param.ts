import { retrieveLaunchParams } from '@telegram-apps/bridge';

interface TgStartParam {
  id: number
  username: string
  first_name: string
  last_name: string
}

function decodeBase64Url<T extends object>(encodedStr: string): T {
  console.log('encodedStr\n', encodedStr)
  let padding = encodedStr.length % 4;
  if (padding !== 0) {
      encodedStr += '='.repeat(4 - padding);
  }
  const base64 = encodedStr.replace(/-/g, '+').replace(/_/g, '/');
  const jsonStr = atob(base64);
  console.log('jsonStr\n', jsonStr)
  console.log('startattach\n', JSON.parse(jsonStr))
  return JSON.parse(jsonStr);
}

export function useTgStartParam() {
  console.log('retrieveLaunchParams\n', retrieveLaunchParams(true))
  const { startattach } = retrieveLaunchParams(true);

  return decodeBase64Url<TgStartParam>(startattach as string)
}