import { retrieveLaunchParams } from '@telegram-apps/bridge';

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

export function useTgUser() {
  console.log('retrieveLaunchParams\n', retrieveLaunchParams(true))
  const launchParams = retrieveLaunchParams(true);
  const receiver = launchParams.tgWebAppData!.user!;
  const startattach = launchParams.startattach as string;
  const sender = decodeBase64Url<TgStartParam>(startattach);
  return { sender, receiver };
}