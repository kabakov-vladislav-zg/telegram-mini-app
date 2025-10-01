import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { useTgUser } from '@/hooks/telegram/use-user';
import axios from 'axios';
import { Button, StyleSheet } from 'react-native';

export default function Index() {
  const { sender, receiver } = useTgUser()

  async function onPress() {
    try {
      await axios.post('/api/custom_method', {
        method: 'send_message_to_user',
        params: {
          sender,
          receiver, 
          message: 'test'
        }
      });
    } catch (error) {
      console.error('❌ Error:', error.response?.data || error.message);
      throw error;
    }
  }
  return (
    <ThemedView style={styles.container}>
      <ThemedText
        type='title'
        style={{ textAlign: 'center' }}
      >
        Анкета для друзей
      </ThemedText>

      <ThemedText>sender</ThemedText>
      <ThemedText>{sender.username}</ThemedText>
      <ThemedText>receiver</ThemedText>
      <ThemedText>{receiver.username}</ThemedText>
      <Button
        title="нажми"
        onPress={onPress}
      />

      {/* <View>
        <Link href="/classic" asChild>
          <Pressable>
            <ThemedText
              type='subtitle'
            >
              Классическая анкета
            </ThemedText>
          </Pressable>
        </Link>
      </View> */}
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