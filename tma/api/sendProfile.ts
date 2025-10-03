  import axios from 'axios';

  export async function sendProfile({
    ownerId,
    ownerName,
    userId,
    userName,
    userUsername,
    profile,
  }: {
    ownerId: number,
    ownerName: string,
    userId: number,
    userName: string,
    userUsername: string,
    profile: object,
  }) {
    try {
      await axios.post('/api/send_profile', {
        ownerId,
        ownerName,
        userId,
        userName,
        userUsername,
        profile,
      });
    } catch (e) {

    }
  }