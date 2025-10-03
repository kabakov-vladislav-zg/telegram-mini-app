import { StyleSheet, Text, type TextProps } from 'react-native';

import { useThemeColor } from '@/hooks/use-theme-color';

export type ThemedTextProps = TextProps & {
  lightColor?: string;
  darkColor?: string;
  type?: 'default' | 'title' | 'defaultSemiBold' | 'subtitle' | 'link';
};

export function ThemedText({
  style,
  lightColor,
  darkColor,
  type = 'default',
  ...rest
}: ThemedTextProps) {
  const color = useThemeColor({ light: lightColor, dark: darkColor }, 'text');

  return (
    <Text
      style={[
        { color },
        styles[type],
        style,
      ]}
      {...rest}
    />
  );
}

const styles = StyleSheet.create({
  default: {
    fontSize: 14,
    lineHeight: 14,
    fontFamily: 'HachiMaruPop_400Regular',
  },
  defaultSemiBold: {
    fontSize: 14,
    lineHeight: 14,
    fontWeight: '600',
    fontFamily: 'HachiMaruPop_400Regular',
  },
  title: {
    fontSize: 24,
    lineHeight: 24,
    fontWeight: 'bold',
    fontFamily: 'HachiMaruPop_400Regular',
  },
  subtitle: {
    fontSize: 18,
    lineHeight: 18,
    fontWeight: 'bold',
    fontFamily: 'HachiMaruPop_400Regular',
  },
  link: {
    fontSize: 16,
    lineHeight: 16,
    color: '#0a7ea4',
    fontFamily: 'HachiMaruPop_400Regular',
  },
});
