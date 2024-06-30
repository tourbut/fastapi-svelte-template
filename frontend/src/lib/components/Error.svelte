<script>
    export let error;
</script>

{#if typeof error.detail === 'string'}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <div>
            {error.detail}
        </div>
    </div>
{:else if typeof error.detail === 'object' && error.detail.length > 0 }
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        {#each error.detail as err, i}
        <div>
            <strong>{err.loc[0]}</strong> : {err.msg}
        </div>
        {/each}
    </div>
{/if}