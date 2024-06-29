<script>
    import fastapi from "$lib/fastapi"
    import Error from "$lib/components/Error.svelte"
    let test = ''
    let error = {detail:[]}

    async function get_test() {
        await fastapi('get', '/', {}, (json) => {
            test = json.message;
        },
        (json_error) => {
            error = json_error
        })
    }

    get_test();

</script>

<Error error={error} />
<h1>{test}</h1>

