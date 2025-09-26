import { ThemedText } from '@/components/themed-text';
import { StyleSheet } from 'react-native';
import { ThemedView } from '@/components/themed-view';

export default function Index() {
  return (
    <ThemedView style={styles.container}>
      <ThemedText>Анкета для друзей</ThemedText>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
});