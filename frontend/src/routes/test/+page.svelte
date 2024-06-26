<script>
    import fastapi from "$lib/api"
    let test = ''
    
    async function get_test() {
        await fastapi('get', '/', {}, (json) => {
            test = json.message;
        })
    }

    get_test();
</script>

<h1>{test}</h1>