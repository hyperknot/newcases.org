import App from './App.svelte';
import data from '../data/country_data.json';

const app = new App({
	target: document.body,
	props: {
		data
	}
});

export default app;
