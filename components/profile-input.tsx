import { ThemedText } from '@/components/themed-text';
import type { ProfileQuestion } from '@/constants/profiles';
import { useState } from 'react';
import { StyleSheet, TextInput, type TextInputProps, View } from 'react-native';

export type ProfileInputProps = TextInputProps & {
  qustion: ProfileQuestion
};

export default function ProfileInput({
  qustion,
  ...props
}: ProfileInputProps) {
  const [height, setHeight] = useState(0);

  return (
    <View>
      <ThemedText
        type='subtitle'
        style={styles.subtitle}
      >
        { qustion.title }
      </ThemedText>
      <TextInput
        {...props}
        multiline={true}
        onContentSizeChange={(event) =>
          setHeight(event.nativeEvent.contentSize.height)
        }
        style={[styles.input, { height: Math.max(35, height) }]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  subtitle: {
    marginBottom: 6,
  },
  input: {
    borderBottomWidth: 1,
    boxShadow: 'none',
    outlineWidth: 0,
    overflow: 'hidden',
    paddingVertical: 12,
    fontFamily: 'HachiMaruPop_400Regular',
    fontSize: 16,
    
  },
});