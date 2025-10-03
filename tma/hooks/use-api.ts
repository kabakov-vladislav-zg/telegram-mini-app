import { useState } from 'react';

export function useApi<P, R>(request: (p: P) => Promise<R>): [
  boolean,
  (p: P) => Promise<R>,
  string,
  () => void,
] {
  const [pending, setPending] = useState(false);
  const [error, setError] = useState('');
  const clearError = () => setError('');
  const makeRequest = async (params: P) => {
    setPending(true);
    const response = await request(params);
    setPending(false);
    return response;
  }

  return [pending, makeRequest, error, clearError]
}
