import { retrieveLaunchParams } from '@telegram-apps/bridge';

interface TgStartParam {
  id: number
  username: string
  firstName: string
  lastName: string
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

export function useTgUser() {
  const launchParams = retrieveLaunchParams(true);
  console.log('launchParams\n', launchParams)
  const user = launchParams.tgWebAppData!.user!;
  const startParam = launchParams.tgWebAppData!.startParam!;
  const owner = decodeBase64Url<TgStartParam>(startParam);
  return { user, owner };
}