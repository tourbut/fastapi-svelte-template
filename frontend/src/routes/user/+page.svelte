<script>
  import { goto } from '$app/navigation';
  import Error from "$lib/components/Error.svelte";
  import { post_user } from "$lib/apis/user";

  let error = {detail:[]}
  let username = ''
  let password1 = ''
  let password2 = ''
  let email = ''

  const handleSubmit = async () => {

    if (password1 !== password2) {
        error={detail: "비밀번호가 일치하지 않습니다."}
        return
    }
    
    let params = {
        username: username,
        password: password1,
        email: email
    }

    let success_callback = (json) => {
            goto('/')
        }

    let failure_callback = (json_error) => {
            error = json_error
        }

    await post_user(params, success_callback, failure_callback);
  }

</script>

<div class="form-container">
    <h5 class="form-title">회원 가입</h5>
    <form method="post" class="form-layout" on:submit|preventDefault={() => {handleSubmit();}}>
      <div>
        <label for="username" class="form-label">사용자 이름</label>
        <input type="text" class="form-input" id="username" bind:value={username}>
      </div>
      <div>
        <label for="password1" class="form-label">비밀번호</label>
        <input type="password" class="form-input" id="password1" bind:value={password1}>
      </div>
      <div>
        <label for="password2" class="form-label">비밀번호 확인</label>
        <input type="password" class="form-input" id="password2" bind:value={password2}>
      </div>
      <div>
        <label for="email" class="form-label">이메일</label>
        <input type="text" class="form-input" id="email" bind:value={email}>
      </div>
      <button type="submit" class="form-button">생성하기</button>
      <Error error={error} />
    </form>
</div>