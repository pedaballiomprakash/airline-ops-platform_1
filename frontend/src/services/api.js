const API_BASE_URL = 'http://localhost:8000';

export const fetchFlights = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/flights`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    const data = await response.json();
    return data.flights;
  } catch (error) {
    console.error('Failed to fetch flights:', error);
    throw error;
  }
};
