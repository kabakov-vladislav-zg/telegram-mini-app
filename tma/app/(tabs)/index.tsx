import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { useTgUser } from '@/hooks/telegram/use-user';
import { supports } from '@telegram-apps/bridge';
import { Button, StyleSheet } from 'react-native';

export default function Index() {
  const { sender, receiver } = useTgUser()

  function onPress() {
    supports('web_app_data_send', '9.1');
    console.log('supports\n', supports('web_app_data_send', '9.1'))
    window.TelegramWebviewProxy.postEvent('web_app_data_send', {
      data: JSON.stringify({
        sender,
        receiver,
      }),
    });
    window.TelegramWebviewProxy.invokeCustomMethod(
      'send_message_to_user',
      {
        sender,
        receiver, 
        message: 'test'
      },
      (error, result) => {
        if (error) {
          alert('Ошибка отправки');
        } else {
          alert('Сообщение отправлено!');
          window.TelegramWebviewProxy.close();
        }
      }
    );
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