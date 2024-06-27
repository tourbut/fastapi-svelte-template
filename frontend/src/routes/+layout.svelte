<script>
    import '../app.css';
    import { APP_NAME,sample_store } from '$lib/stores';
    console.log($sample_store);
</script>
<svelte:head>
	<title>
		{$APP_NAME}
	</title>
</svelte:head>
  
<nav class="bg-gray-800 p-4">
  <div class="container mx-auto flex justify-between items-center">
    <div class="flex space-x-4">
      <a href="/" class="text-gray-300 hover:text-white">Home</a>
      <a href="/test" class="text-gray-300 hover:text-white">Test</a>
      <a href="/user" class="text-gray-300 hover:text-white">User</a>
    </div>
  </div>
</nav>

<slot></slot>