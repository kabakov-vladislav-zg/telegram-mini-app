export type ProfileQuestion = {
  id: string,
  title: string,
  type: string,
  variants?: string[],
}

export const ProfileQuestions: ProfileQuestion[] = [
  {
    id: 'name',
    title: 'Имя',
    type: 'text',
  },
  {
    id: 'nickname',
    title: 'Как тебя называют друзья',
    type: 'text',
  },
  {
    id: 'birthday',
    title: 'День рождения',
    type: 'date',
  },
  {
    id: 'eyecolor',
    title: 'Какой у тебя цвет глаз',
    type: 'select',
    variants: [],
  },
]