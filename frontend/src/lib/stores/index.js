import { writable } from 'svelte/store';
import { WEB_NAME } from '$lib/constants';

export const APP_NAME = writable(WEB_NAME);
export const sample_store = writable('sample store value');