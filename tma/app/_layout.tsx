import { ThemedView } from '@/components/themed-view';
import { useInitApp } from '@/hooks/telegram/use-init-app';
import { useColorScheme } from '@/hooks/use-color-scheme';
import { HachiMaruPop_400Regular, useFonts } from '@expo-google-fonts/hachi-maru-pop';
import { DarkTheme, DefaultTheme, ThemeProvider } from '@react-navigation/native';
import { Stack } from 'expo-router';
import { ActivityIndicator, StyleSheet } from 'react-native';
import 'react-native-reanimated';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';

export default function RootLayout() {
  const colorScheme = useColorScheme();
  const initialized = useInitApp();
  const [fontsLoaded] = useFonts({
    HachiMaruPop_400Regular,
  });

  const isReady = fontsLoaded && initialized;
  return (
    <ThemeProvider value={colorScheme === 'dark' ? DarkTheme : DefaultTheme}>
      <SafeAreaProvider>
        <SafeAreaView style={styles.container}>
          {isReady ? (
            <Stack screenOptions={{ headerShown: false }}>
              <Stack.Screen name="(tabs)" />
            </Stack>
          ) : (
            <ThemedView style={styles.preloader}>
              <ActivityIndicator size="large" color="#0000ff" />
            </ThemedView>
          )}
        </SafeAreaView>
      </SafeAreaProvider>
    </ThemeProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  preloader: {
    flex: 1,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
});