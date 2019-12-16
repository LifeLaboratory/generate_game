import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'game'
        self.field = ['name', 'description', 'id_user', 'rate']

    def create(self, data):
        self.query = f'''
  insert into "{self.table_name}"
  (name, description, id_user)
  values (
    '{data.get('name')}'
    , '{data.get('description')}'
    , {data.get('id_user')}
  )
  returning id_game
'''
        return self.execute()

    def login(self, data):
        where = f'''
  where true
    and '{data.get('login')}' = "login"
    and '{data.get('password')}' = "password"
        '''
        user = self.games(where)
        return user[0] if user else None

    def game(self, id_game):
        where = f'where id_game = {id_game}'
        limit = f'limit 1'
        return self.games(where, limit)

    def user_game(self, id_user):
        where = f'where id_user = {id_user}'
        return self.games(where)

    def games(self, where=None, limit=None):
        self.query = f'''
  select 
    id_game
    , g.name
    , description
    , rate
    , n.id_user
    , n.name as name_user
  from "{self.table_name}" g
  left join "user" u using("id_user")
  {where}
  order by rate desc
  {limit}
        '''
        return self.execute()
