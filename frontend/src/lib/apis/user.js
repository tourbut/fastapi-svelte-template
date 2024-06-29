import fastapi from "$lib/fastapi";

export async function post_user(params, success_callback, failure_callback) {
    
    let url = "/users/asignup/"

    await fastapi('post', url, params,success_callback,failure_callback)
}