# Instasport_test

Quick notes:
 - Made 2 scenarios available(group and personal workouts) for group workout just don't specify user
 - Made API (api folder) so functionality asked in the task is available through requests only
 - Made web app (app folder) mostly it's just copypasted from api but returns web pages and redirects when needed instead of DRF Response
 - Write some simple web pages(need to slightly develop my css skills)
 - Added celery cron to clear all tasks which already started(clear all twice a hour)
 - Writed my first class-based views(previously was working with function based)
 - Didn't make different level of permissions because django admin already have limited access(I know how to add them to views)
 - Usually i write tests(check other test tasks) but this task is very small, so i just manually tested it
 
 Models:
 <table>
  <tr>
    <td><b>Model</b></td><td><b>Fields</b></td><td><b>To create</b></td>
  </tr>
  <tr>
    <td>User(username field - email)</td><td>email(unique), username</td><td> email, username, password, (to create superuser(admin): is_staff=True, is_superuser=True)</td>
  </tr>
  <tr>
    <td>Workout</td><td>user(optional), time, name</td><td>user(optional), time, name</td>
  </tr>
  </table>
  
  User creation is available via api/register, login via api/login, logout via api/logout
