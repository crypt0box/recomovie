export default function ({ redirect }) {
  // ユーザーが認証されていないとき
  if (!localStorage.getItem('idToken')) {
    return redirect('/login')
  }
}