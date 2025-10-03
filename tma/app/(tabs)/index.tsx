import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { useTgUser } from '@/hooks/telegram/use-user';
import { Link } from 'expo-router';
import { Button, StyleSheet, View } from 'react-native';

export default function Index() {
  const { owner } = useTgUser()
  return (
    <ThemedView style={styles.container}>
      <ThemedText
        type='title'
        style={{ textAlign: 'center' }}
      >
        Анкета для друзей
      </ThemedText>
      <View style={styles.section}>
        <ThemedText type='defaultSemiBold'>
          Обо мне:
        </ThemedText>
        <ThemedText>
          Имя: { owner.firstName }
        </ThemedText>
        <ThemedText>
          Ник: { owner.username }
        </ThemedText>
      </View>
      <View style={styles.section}>
        <ThemedText type='defaultSemiBold'>
          Тут можно:
        </ThemedText>
        <Link href="/profile" asChild>
          <Button
            title='Заполнить анкету'
          />
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
  section: {
    gap: 16,
  },
});