import { emitEvent, mockTelegramEnv } from '@telegram-apps/bridge';

const noInsets = {
  left: 0,
  top: 0,
  bottom: 0,
  right: 0,
} as const;

const themeParams = {
  accentTextColor: "#168acd",
  bgColor: "#ffffff",
  bottomBarBgColor: "#ffffff",
  buttonColor: "#40a7e3",
  buttonTextColor: "#ffffff",
  destructiveTextColor: "#d14e4e",
  headerBgColor: "#ffffff",
  hintColor: "#999999",
  linkColor: "#168acd",
  secondaryBgColor: "#f1f1f1",
  sectionBgColor: "#ffffff",
  sectionHeaderTextColor: "#168acd",
  sectionSeparatorColor: "#e7e7e7",
  subtitleTextColor: "#999999",
  textColor: "#000000",
} as const;

const tgWebAppData = [
  ['user', JSON.stringify({
    added_to_attachment_menu: false,
    allows_write_to_pm: false,
    is_premium: false,
    is_bot: false,
    id: 1,
    username: 'Pavel_Pavelov',
    first_name: 'Pavel',
    last_name: 'Pavelov',
    language_code: 'ru',
    photo_url: '',
  })],
  ['startParam', 'eyJpZCI6MTQ3NDU3MzQ2MiwiaXNfYm90IjpmYWxzZSwiZmlyc3RfbmFtZSI6Ilx1MDQxMlx1MDQzYlx1MDQzMFx1MDQzNFx1MDQzOFx1MDQ0MVx1MDQzYlx1MDQzMFx1MDQzMiIsImxhc3RfbmFtZSI6bnVsbCwidXNlcm5hbWUiOiJWbGFkaXNsYXZfS2FiYWtvdiIsImxhbmd1YWdlX2NvZGUiOiJydSJ9'],
  ['hash', ''],
  ['signature', ''],
  ['auth_date', Date.now().toString()],
];

export function appMockTelegramEnv(): void {
  mockTelegramEnv({
    launchParams: {
      tgWebAppThemeParams: themeParams,
      tgWebAppData: new URLSearchParams(tgWebAppData),
      tgWebAppVersion: '8',
      tgWebAppPlatform: 'tdesktop',
    },
    onEvent(e) {
      if (e[0] === 'web_app_request_theme') {
        return emitEvent('theme_changed', { theme_params: themeParams });
      }
      if (e[0] === 'web_app_request_viewport') {
        return emitEvent('viewport_changed', {
          height: window.innerHeight,
          width: window.innerWidth,
          is_expanded: true,
          is_state_stable: true,
        });
      }
      if (e[0] === 'web_app_request_content_safe_area') {
        return emitEvent('content_safe_area_changed', noInsets);
      }
      if (e[0] === 'web_app_request_safe_area') {
        return emitEvent('safe_area_changed', noInsets);
      }
    },
  });
}