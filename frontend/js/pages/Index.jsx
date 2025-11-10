
import { Link } from "@inertiajs/react";

export default function Index({ heroes }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-white mb-4">
            Heroes Roster
          </h1>
          <p className="text-xl text-gray-300">
            Los mejores héroes del universo
          </p>
          <div className="mt-2 text-gray-400">
            Total de héroes: <span className="text-purple-400 font-semibold">{heroes?.length || 0}</span>
          </div>
        </div>

        {/* Heroes Grid */}
        {heroes && heroes.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {heroes.map((hero) => (
              <div
                key={hero.id}
                className="bg-slate-800/50 backdrop-blur-sm rounded-lg overflow-hidden border border-purple-500/20 hover:border-purple-500/50 transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-purple-500/20"
              >
                {/* Hero Image */}
                <div className="relative h-64 bg-gradient-to-b from-purple-900/20 to-slate-900">
                  {hero.profileImage ? (
                    <img
                      src={hero.profileImage}
                      alt={hero.name}
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <div className="w-full h-full flex items-center justify-center">
                      <div className="text-6xl text-purple-400/30">👤</div>
                    </div>
                  )}
                  {/* Power Level Badge */}
                  <div className="absolute top-3 right-3 bg-purple-600/90 backdrop-blur-sm px-3 py-1 rounded-full">
                    <span className="text-white font-bold text-sm">
                      ⚡ {hero.powerLevel}
                    </span>
                  </div>
                </div>

                {/* Hero Info */}
                <div className="p-5">
                  <h3 className="text-2xl font-bold text-white mb-1">
                    {hero.name}
                  </h3>
                  {hero.realName && (
                    <p className="text-gray-400 text-sm mb-3">
                      {hero.realName}
                    </p>
                  )}

                  {/* Universe Badge */}
                  <div className="mb-3">
                    <span className="inline-block bg-blue-600/20 text-blue-300 px-3 py-1 rounded-full text-xs font-semibold border border-blue-500/30">
                      {hero.universe}
                    </span>
                  </div>

                  {/* Powers */}
                  {hero.powers && hero.powers.length > 0 && (
                    <div className="mb-4">
                      <h4 className="text-xs font-semibold text-gray-400 mb-2">
                        PODERES:
                      </h4>
                      <div className="flex flex-wrap gap-1">
                        {hero.powers.slice(0, 3).map((power, idx) => (
                          <span
                            key={idx}
                            className="inline-block bg-purple-600/20 text-purple-300 px-2 py-1 rounded text-xs border border-purple-500/30"
                          >
                            {power}
                          </span>
                        ))}
                        {hero.powers.length > 3 && (
                          <span className="inline-block bg-purple-600/20 text-purple-300 px-2 py-1 rounded text-xs border border-purple-500/30">
                            +{hero.powers.length - 3} más
                          </span>
                        )}
                      </div>
                    </div>
                  )}

                  {/* Action Link */}
                  <Link 
                    href={`/${hero.id}`}
                    className="block w-full text-center px-4 py-2 rounded-md bg-purple-600/10 hover:bg-purple-600/30 text-purple-300 border border-purple-500/30 hover:border-purple-500/50 transition-all font-medium"
                  >
                    Ver Detalles
                  </Link>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-20">
            <div className="text-6xl mb-4">🦸</div>
            <p className="text-2xl text-gray-400 mb-4">
              No hay héroes disponibles
            </p>
            <p className="text-gray-500">
              Ejecuta el comando seed para agregar héroes a la base de datos
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
