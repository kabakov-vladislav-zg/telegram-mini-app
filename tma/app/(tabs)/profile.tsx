import { sendProfile } from '@/api/sendProfile';
import ProfileInput from '@/components/profile-input';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { ProfileQuestions } from '@/constants/profile';
import { useTgUser } from '@/hooks/telegram/use-user';
import { useApi } from '@/hooks/use-api';
import { useState } from 'react';
import { Button, StyleSheet } from 'react-native';

export default function Index() {
  const initForm = Object.fromEntries(ProfileQuestions.map(({ id }) => [id, '']));
  const [form, setForm] = useState(initForm);
  const { user, owner } = useTgUser()
  const [pending, makeRequest] = useApi(sendProfile)

  function setField(key: string, value: string) {
    setForm(form => ({ ...form, [key]: value }));
  }
  function onSubmit() {
    makeRequest({
      ownerId: owner.id,
      ownerName: owner.firstName,
      userId: user.id,
      userName: user.firstName,
      userUsername: user.firstName,
      profile: form,
    })
  }
  return (
    <ThemedView style={styles.container}>
      <ThemedText type='title'>Анкета</ThemedText>
      
      {ProfileQuestions.map(q =>
        <ProfileInput
          key={q.id}
          qustion={q}
          value={form[q.id]}
          onChangeText={(value) => setField(q.id, value)}
        />
      )}
      <Button
        title='Оставить секретную записку'
        disabled={pending}
        onPress={onSubmit}
      />
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    padding: 12,
    gap: 16,
  },
});