import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { Pressable, StyleSheet, View } from 'react-native';

export default function Index() {
  return (
    <ThemedView style={styles.container}>
      <ThemedText
        type='title'
        style={{ textAlign: 'center' }}
      >
        Анкета для друзей
      </ThemedText>
      <View>
        <Link href="/classic" asChild>
          <Pressable>
            <ThemedText
              type='subtitle'
            >
              Классическая анкета
            </ThemedText>
          </Pressable>
        </Link>
      </View>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    padding: 12,
    gap: 24,
  },
});