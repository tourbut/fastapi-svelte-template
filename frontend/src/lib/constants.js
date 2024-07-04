import { dev } from '$app/environment';

export const WEB_NAME = 'Knowslog Template Web';
export const FASTAPI_BASE_URL = dev ? 'http://localhost:8000' : '';
export const API_URL = `${FASTAPI_BASE_URL}/api/v1`;