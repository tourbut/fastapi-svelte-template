<script>
    let test = ''

    function get_test() {
        fetch("http://127.0.0.1:8000/").then((res) => {
            res.json().then((json) => {
                test = json.message;
            });
        });
    }
  
    get_test();
</script>

<h1>{test}</h1>