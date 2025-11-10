import { Link } from "@inertiajs/react";

export default function Detail({ character }) {
  return (
    <div className="min-h-screen bg-slate-950">
      {/* Hero Header with Background Image */}
      <div 
        className="relative h-96 bg-cover bg-center"
        style={{
          backgroundImage: character.backgroundImage 
            ? `url(${character.backgroundImage})` 
            : 'linear-gradient(to bottom, rgba(51, 65, 85, 0.5), rgba(15, 23, 42, 1))'
        }}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-transparent to-slate-950"></div>
        
        {/* Back Link */}
        <div className="absolute top-6 left-6 z-10">
          <Link 
            href="/"
            className="inline-flex items-center px-4 py-2 rounded-md bg-slate-800 hover:bg-slate-700 text-white border border-slate-700 hover:border-slate-600 transition-all font-medium"
          >
            ← Volver al Roster
          </Link>
        </div>

        {/* Hero Title */}
        <div className="absolute bottom-0 left-0 right-0 p-8">
          <div className="container mx-auto">
            <div className="flex items-end gap-6">
              {/* Profile Image */}
              {character.profileImage && (
                <div className="w-40 h-40 rounded-lg overflow-hidden border-4 border-slate-700 shadow-2xl">
                  <img 
                    src={character.profileImage} 
                    alt={character.name}
                    className="w-full h-full object-cover"
                  />
                </div>
              )}
              
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
                  <span className="px-3 py-1 bg-slate-700 text-white rounded-full text-sm font-semibold">
                    {character.type}
                  </span>
                  <span className="px-3 py-1 bg-blue-600 text-white rounded-full text-sm font-semibold">
                    {character.universe}
                  </span>
                  <span className="px-3 py-1 bg-emerald-600 text-white rounded-full text-sm font-semibold">
                    ⚡ {character.powerLevel}
                  </span>
                </div>
                <h1 className="text-5xl font-bold text-white mb-2">
                  {character.name}
                </h1>
                {character.realName && (
                  <p className="text-2xl text-slate-300">
                    {character.realName}
                  </p>
                )}
                {character.alias && (
                  <p className="text-lg text-slate-400 mt-1">
                    También conocido como: {character.alias}
                  </p>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Column */}
          <div className="lg:col-span-2 space-y-6">
            {/* Biography */}
            {character.biography && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-2xl font-bold text-white mb-4">Biografía</h2>
                <p className="text-slate-300 leading-relaxed whitespace-pre-line">
                  {character.biography}
                </p>
              </div>
            )}

            {/* Background Story */}
            {character.backgroundStory && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-2xl font-bold text-white mb-4">Historia de Origen</h2>
                <p className="text-slate-300 leading-relaxed whitespace-pre-line">
                  {character.backgroundStory}
                </p>
              </div>
            )}

            {/* Notable Quotes */}
            {character.notableQuotes && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-2xl font-bold text-white mb-4">Frases Célebres</h2>
                <div className="space-y-3">
                  {character.notableQuotes.split('\n').filter(q => q.trim()).map((quote, idx) => (
                    <div key={idx} className="border-l-4 border-blue-500 pl-4 py-2">
                      <p className="text-slate-300 italic">"{quote}"</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Allies */}
            {character.allies && character.allies.length > 0 && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-2xl font-bold text-white mb-4">Aliados</h2>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                  {character.allies.map((ally) => (
                    <Link 
                      key={ally.id} 
                      href={`/${ally.id}`}
                      className="flex items-center gap-3 p-3 bg-slate-700 rounded-lg hover:bg-slate-600 transition-colors"
                    >
                      {ally.profileImage ? (
                        <img 
                          src={ally.profileImage} 
                          alt={ally.name}
                          className="w-12 h-12 rounded-full object-cover"
                        />
                      ) : (
                        <div className="w-12 h-12 rounded-full bg-slate-600 flex items-center justify-center">
                          <span className="text-2xl">👤</span>
                        </div>
                      )}
                      <span className="text-white font-medium text-sm">{ally.name}</span>
                    </Link>
                  ))}
                </div>
              </div>
            )}

            {/* Enemies */}
            {character.enemies && character.enemies.length > 0 && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-2xl font-bold text-white mb-4">Enemigos</h2>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                  {character.enemies.map((enemy) => (
                    <Link 
                      key={enemy.id} 
                      href={`/${enemy.id}`}
                      className="flex items-center gap-3 p-3 bg-slate-700 rounded-lg hover:bg-slate-600 transition-colors"
                    >
                      {enemy.profileImage ? (
                        <img 
                          src={enemy.profileImage} 
                          alt={enemy.name}
                          className="w-12 h-12 rounded-full object-cover"
                        />
                      ) : (
                        <div className="w-12 h-12 rounded-full bg-slate-600 flex items-center justify-center">
                          <span className="text-2xl">👤</span>
                        </div>
                      )}
                      <span className="text-white font-medium text-sm">{enemy.name}</span>
                    </Link>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Basic Info */}
            <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
              <h2 className="text-xl font-bold text-white mb-4">Información</h2>
              <div className="space-y-3">
                {character.species && (
                  <div>
                    <span className="text-slate-400 text-sm">Especie:</span>
                    <p className="text-white">{character.species}</p>
                  </div>
                )}
                {character.gender && (
                  <div>
                    <span className="text-slate-400 text-sm">Género:</span>
                    <p className="text-white">{character.gender}</p>
                  </div>
                )}
                {character.occupation && (
                  <div>
                    <span className="text-slate-400 text-sm">Ocupación:</span>
                    <p className="text-white">{character.occupation}</p>
                  </div>
                )}
                {character.status && (
                  <div>
                    <span className="text-slate-400 text-sm">Estado:</span>
                    <p className="text-white">{character.status}</p>
                  </div>
                )}
                {character.baseOfOperations && (
                  <div>
                    <span className="text-slate-400 text-sm">Base de Operaciones:</span>
                    <p className="text-white">{character.baseOfOperations}</p>
                  </div>
                )}
              </div>
            </div>

            {/* Powers */}
            {character.powers && character.powers.length > 0 && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-xl font-bold text-white mb-4">Poderes</h2>
                <div className="space-y-3">
                  {character.powers.map((power) => (
                    <div 
                      key={power.id}
                      className="p-3 bg-slate-700 rounded-lg"
                    >
                      <h3 className="text-white font-semibold mb-1">{power.name}</h3>
                      {power.description && (
                        <p className="text-slate-400 text-sm">{power.description}</p>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Affiliations */}
            {character.affiliations && character.affiliations.length > 0 && (
              <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
                <h2 className="text-xl font-bold text-white mb-4">Afiliaciones</h2>
                <div className="space-y-2">
                  {character.affiliations.map((aff) => (
                    <div 
                      key={aff.id}
                      className="p-3 bg-slate-700 rounded-lg"
                    >
                      <h3 className="text-white font-semibold">{aff.name}</h3>
                      <p className="text-slate-400 text-xs">{aff.type}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Meta Information */}
            <div className="bg-slate-800 rounded-lg p-6 border border-slate-700">
              <h2 className="text-xl font-bold text-white mb-4">Detalles de Publicación</h2>
              <div className="space-y-3">
                {character.firstAppearance && (
                  <div>
                    <span className="text-slate-400 text-sm">Primera Aparición:</span>
                    <p className="text-white text-sm">{character.firstAppearance}</p>
                  </div>
                )}
                {character.createdBy && (
                  <div>
                    <span className="text-slate-400 text-sm">Creado por:</span>
                    <p className="text-white text-sm">{character.createdBy}</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

