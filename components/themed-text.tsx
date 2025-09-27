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
    fontSize: 16,
    lineHeight: 16,
  },
  defaultSemiBold: {
    fontSize: 16,
    lineHeight: 16,
    fontWeight: '600',
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
  },
});
