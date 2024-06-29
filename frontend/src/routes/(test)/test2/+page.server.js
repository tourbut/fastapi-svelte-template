export async function load() {
    const response = await fetch('http://localhost:8000/');  // FastAPI 엔드포인트 호출
    const data = await response.json();
    return {
        message: data.message
    };
  }