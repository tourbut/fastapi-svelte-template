import { dev } from '$app/environment';

export const WEB_NAME = 'Knowslog Template Web';
export const FASTAPI_BASE_URL = dev ? `http://localhost:8000` : `http://fastapi:8000`;